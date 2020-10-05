import React, { Component, useState, useEffect } from "react";
import axios from "axios";
import Slider from "react-slick";
import "../css/index-slider.css";

class MainSlider extends Component {
  render() {
    const { products } = this.props;

    const settings = {
      slidesToShow: 4,
      slidesToScroll: 4,
    };

    return (
      <div class="index__slider">
        <Slider {...settings}>
          {products.map((product) => (
            <a href={"products/" + product.slug + "/"}>
              <img src={product.img} alt="Product IMG" class="index__slide--img" />
              <div class="index__slideBox">
                <div class="index__slide--header">
                  <span class="index__slide--name">{product.name}</span>
                  <div>
                    <img class="index__slide--good" src="/images/thumb_up_alt-24px.png"></img>
                    <span>{product.like.length}</span>
                  </div>
                </div>
                <div class="index__slide--description">
                  <p>{product.description}</p>
                </div>
              </div>
            </a>
          ))}
        </Slider>
      </div>
    );
  }
}

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
        <img src="/images/point.png" className="point" alt="point" />
        {title}
      </span>
      {search && <Search />}
    </div>
  );
};

const MainIndex = () => {
  const [productsBest, setProductsBest] = useState([]);
  const [productsList, setProductsList] = useState([]);

  useEffect(() => {
    getProductsBest();
    getProductsList();
  }, []);

  const getProductsBest = async () => {
    const { data } = await axios.get("/api/products-best/");
    setProductsBest(data);
  };

  const getProductsList = async () => {
    const { data } = await axios.get("/api/products-list/");
    setProductsList(data);
  };

  return (
    <div className="index">
      <MainIndexTitle title="베스트 상품" search={true} />
      <MainSlider products={productsBest} />
      <MainIndexTitle title="전체 상품" search={false} />
      <MainSlider products={productsList} />
      <img class="index__banner" src="/images/sub__bn.png"></img>
    </div>
  );
};

export default MainIndex;
