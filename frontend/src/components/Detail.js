import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const Detail = () => {
  let { slug } = useParams();
  const [productDetail, setProductDetail] = useState();

  useEffect(() => {
    getProduct();
  }, []);

  const getProduct = async () => {
    const { data } = await axios.get("/api/products/" + slug);
    console.log(data.category.first);
    setProductDetail(data);
  };

  return (
    <main className="detail">
      <div className="detailBox">
        <div className="detail__leftContent">
          <span className="detail__title">
            {productDetail ? productDetail.category.first : null}
          </span>
        </div>
      </div>
    </main>
  );
};

export default Detail;
