import React, { useState, useEffect } from "react";
import axios from "axios";

const MainSlider = ({ products }) => {
  return (
    <div class="index__slider index__best">
      {products.map((product) => (
        <span>{product.name}</span>
      ))}
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
        <img src="/images/point.png" className="point" alt="point" />
        {title}
      </span>
      {search && <Search />}
    </div>
  );
};

const MainIndex = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    getProducts();
  }, []);

  const getProducts = async () => {
    const { data } = await axios.get("/api/products/");
    setProducts(data);
  };

  return (
    <div className="index">
      <MainIndexTitle title="베스트 상품" search={true} />
      <MainSlider products={products} />
    </div>
  );
};

export default MainIndex;
