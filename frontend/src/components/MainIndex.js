import React from "react";

const MainSlider = () => {
  return (
    <div class="index__slider index__best">
      {% for product in best_products %}
      <a href="{{product.get_absolute_url}}">
        <img src="{{product.image_url}}" alt="Product IMG" class="index__slide--img" />
        <div class="index__slideBox">
          <div class="index__slide--header">
            <span class="index__slide--name">{{product.name}}</span>
            <div>
              <img class="index__slide--good" src="{% static 'logo/thumb_up_alt-24px.png' %}"></img>
              <span>{{ product.like.count }}</span>
            </div>
          </div>
          <div class="index__slide--description"><p>{{product.description}}</p></div>
        </div>
      </a>
      {% endfor %}
    </div>
  );
};

const Search = () => {
  return (
    <form method="get">
      <div className="index__header--search">
        <input autocomplete="off" type="text" name="q" id="search-bar" placeholder="Search" />
        <button>
          <i className="fas fa-search"></i>
        </button>
      </div>
    </form>
  );
};

const MainIndexTitle = ({ title, search }) => {
  return (
    <div className="index__header">
      <span className="index__header--title">
        <img src="/images/point.png" className="point" />
        {title}
      </span>
      {search && <Search />}
    </div>
  );
};

const MainIndex = () => {
  return (
    <div className="index">
      <MainIndexTitle title="베스트 상품" search={true} />
    </div>
  );
};

export default MainIndex;
