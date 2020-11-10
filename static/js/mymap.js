var infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new kakao.maps.LatLng(37.566826, 126.9786567), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };
var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다
// 일반 지도와 스카이뷰로 지도 타입을 전환할 수 있는 지도타입 컨트롤을 생성합니다
var mapTypeControl = new kakao.maps.MapTypeControl();
// 지도에 컨트롤을 추가해야 지도위에 표시됩니다
// kakao.maps.ControlPosition은 컨트롤이 표시될 위치를 정의하는데 TOPRIGHT는 오른쪽 위를 의미합니다
map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);
// 지도 확대 축소를 제어할 수 있는  줌 컨트롤을 생성합니다
var zoomControl = new kakao.maps.ZoomControl();
map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);
// 장소 검색 객체를 생성합니다
var ps = new kakao.maps.services.Places(map);

// 마커 이미지
var mapContainer = document.getElementById('map');
var imageSrc = mapContainer.getAttribute('marker-url');

var imageSize = new kakao.maps.Size(30, 30);
var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);

var markers = [];
var myMarkers = [];
var myList = [ //api에서 얻어온 것으로 가정
    {
        place_name: 'GS25 서울역점',
        y: 37.554048557232754,
        x: 126.97233189463573
    },

];
function enterkey() {// 엔터키가 누르면 검색 (검색창)
    if (window.event.keyCode == 13) {
        findPlace();
    }
}
//내편 목록에 있으면 인덱스를, 없으면 -1을 반환
function inMyList(name) {
    var idx = tempList.findIndex(i => i.place_name == name);
    return idx;
}
//1. 내편 목록에 있는지 확인
//findIndex가 -1이 아니면 존재


var cvsInfo = document.getElementById("cvsInfo"),
    infoTitle = document.getElementById("info-title"),
    infoMy = document.getElementById("info-my"),
    infoNotMy = document.getElementById("info-not-my"),
    infoAddress = document.getElementById("info-address"),
    infoPhone = document.getElementById("info-phone"),
    infoUrl = document.getElementById("info-url"),
    infoRoute = document.getElementById("info-route"),
    myCvsList = document.getElementById("myCvsList");

//정보 창에 출력하기
function makeInfo(place) {
    if (inMyList(place.place_name) > -1) {
        infoMy.style.display = "block";
        infoNotMy.style.display = "none";
    } else {
        infoMy.style.display = "none";
        infoNotMy.style.display = "block";
    }
    console.log(inMyList(place.place_name))
    infoTitle.innerText = place.place_name;
    infoAddress.innerText = place.road_address_name;
    //x,y 좌표 저장
    infoAddress.setAttribute('x', place.x);
    infoAddress.setAttribute('y', place.y);
    //
    infoPhone.innerText = place.phone;
    infoUrl.href = place.place_url;
    infoRoute.href = "https://map.kakao.com/link/to/" + place.id;
    cvsInfo.style.visibility = "visible";
}

//내편목록 마커 찍기
setMyList(tempList);
function setMyList(list) {
    console.log(list)
    var content = "";
    for (var i = 0; i < list.length; i++) {
        console.log(list[i]);
        console.log(typeof (list[i].x))
        // <button onclick="myCVS(this)">이마트24 서울시청점</button></li>
        content += '<li class="list-group-item" onclick="myCVS(this)">' //정보 창 생성 함수 연결
            + list[i].place_name + '</li>'
        addMyMarker(list[i]);
    }
    myCvsList.innerHTML = content;
}

function infoclick() {
    //infowindow에서 편의점 이름 가져오기
    var cvsName = document.getElementById("info-window").innerText;

    // 편의점 이름으로 검색해서 창 띄우기
    ps.keywordSearch(cvsName, infoSearchCB);
}

//2. 내편 목록에 추가
//배열에 추가, setMyList
function addMyCvs() {
    var place = {
        place_name: infoTitle.innerText,
        x: Number(infoAddress.getAttribute('x')),
        y: Number(infoAddress.getAttribute('y'))
    }
    myList.push(place);
    hideMyMarkers();
    myMarkers = [];

    setMyList(myList);

    //ajax 로직 추가
    infoMy.style.display = "block";
    infoNotMy.style.display = "none";
}
//3. 내편 목록에서 삭제
//findIndex 반환값으로 splice(idx,1) , setMyList
function delMyCvs() {
    place_name = infoTitle.innerText;
    var idx = inMyList(place_name);
    console.log(idx);
    myList.splice(idx, 1);

    hideMyMarkers();
    myMarkers = [];

    setMyList(myList);
    // myMarkers = null;

    setMyMarkers(map);
    //ajax 로직 추가
    infoMy.style.display = "none";
    infoNotMy.style.display = "block";

}
// 마커를 생성하고 지도위에 표시하는 함수입니다
function addMarker(place) {

    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        position: new kakao.maps.LatLng(place.y, place.x),
        clickable: true
    });
    var infowindowContent = '<div id="info-window" onclick="infoclick()">' + place.place_name + '</div>';
    // 마커에 mouseover & infowindow를 등록합니다
    kakao.maps.event.addListener(marker, 'mouseover', function () {
        infowindow.setContent(infowindowContent);
        infowindow.open(map, marker);
    });
    // 마커가 지도 위에 표시되도록 설정합니다
    marker.setMap(map);

    // 생성된 마커를 배열에 추가합니다
    markers.push(marker);
}

// 마커를 생성하고 지도위에 표시하는 함수입니다
function addMyMarker(place) {
    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        // map: map,
        position: new kakao.maps.LatLng(place.y - 0.00005, place.x),
        clickable: true,
        image: markerImage // 마커 이미지
    });
    marker.setOpacity(0.7);
    // 마커가 지도 위에 표시되도록 설정합니다
    marker.setMap(map); // marker 안에 map 설정 하는 것과 차이..?
    var infowindowContent = '<div id="info-window" style="padding:10px;font-size:18px;" onclick="infoclick()">' + place.place_name + '</div>';
    // 마커에 mouseover & infowindow를 등록합니다
    kakao.maps.event.addListener(marker, 'mouseover', function () {
        infowindow.setContent(infowindowContent);
        infowindow.open(map, marker);
    });
    // 생성된 마커를 배열에 추가합니다
    myMarkers.push(marker);
}
// 배열에 추가된 마커들을 지도에 표시하거나 삭제하는 함수입니다
function setMarkers(map) {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(map);
    }
}

// 배열에 추가된 마커를 지도에 표시하는 함수입니다
function showMarkers() {
    setMarkers(map)
}

//배열에 추가된 마커를 지도에서 삭제하는 함수입니다
function hideMarkers() {
    setMarkers(null);
}
// 배열에 추가된 마커들을 지도에 표시하거나 삭제하는 함수입니다
function setMyMarkers(map) {
    for (var i = 0; i < myMarkers.length; i++) {
        myMarkers[i].setMap(map);
    }
}

// 배열에 추가된 마커를 지도에 표시하는 함수입니다
function showMarkers() {
    setMyMarkers(map)
}

// 배열에 추가된 마커를 지도에서 삭제하는 함수입니다
function hideMyMarkers() {
    setMyMarkers(null);
}
var inputPlace = document.getElementById("inputPlace"); //검색창
function findPlace() {

    var place = inputPlace.value;
    if (place == "") {
        return false;
    }
    hideMarkers();
    ps.keywordSearch(place + " 편의점", placeNameSearchCB);
}

// 장소 이름으로 검색하는 함수
function placeNameSearchCB(data, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {

        // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
        // LatLngBounds 객체에 좌표를 추가합니다
        var bounds = new kakao.maps.LatLngBounds();

        for (var i = 0; i < data.length; i++) {
            //add marker
            addMarker(data[i]);
            bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
            console.log(data[i].place_name);
            console.log(data[i].x);
            console.log(data[i].y);
        }

        // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
        map.setBounds(bounds);
    }
}

// 키워드 검색 완료 시 호출되는 콜백함수 입니다
function placesSearchCB(data, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {
        for (var i = 0; i < data.length; i++) {
            //add marker
            addMarker(data[i]);
        }
    }
}

function mySearchCB(data, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {
        // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
        // LatLngBounds 객체에 좌표를 추가합니다
        var bounds = new kakao.maps.LatLngBounds();
        var x = Number(data[0].x);
        var y = Number(data[0].y);
        bounds.extend(new kakao.maps.LatLng(y, x));

        // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
        map.setBounds(bounds);

        //data[0]으로 창 띄우기
        makeInfo(data[0]);
    }
}

function infoSearchCB(data, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {
        // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
        // LatLngBounds 객체에 좌표를 추가합니다
        var bounds = new kakao.maps.LatLngBounds();
        var x = Number(data[0].x);
        var y = Number(data[0].y);
        bounds.extend(new kakao.maps.LatLng(y, x));

        //data[0]으로 창 띄우기
        makeInfo(data[0]);
    }
}

function findCVS() {
    hideMarkers();
    ps.categorySearch('CS2', placesSearchCB, { useMapBounds: true });
}

function myCVS(elemnt) {
    var placeName = elemnt.innerHTML;
    console.log(placeName);
    ps.keywordSearch(placeName, mySearchCB);
    // 정보창 연결
}
