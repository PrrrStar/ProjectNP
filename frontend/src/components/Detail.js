import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const Detail = () => {
  let { slug } = useParams();
  const [productDetail, setProductDetail] = useState([]);

  useEffect(() => {
    getProduct();
  }, []);

  const getProduct = async () => {
    const { data } = await axios.get("/api/products/" + slug);
    setProductDetail(data);
  };

  let subCategory = document.querySelector(".category__children");

  return (
    <main className="detail">
      {productDetail.category_name}
    </main>
  );
};

export default Detail;
