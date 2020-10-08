import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import "../css/detail.css";

const DetailBox = ({ product }) => {
  return (
    <div className="detailBox">
      <div className="detail__leftContent">
        <span className="detail__title">
          {product ? product.category.first : null}
          <span> &gt; {product ? product.category.second : null}</span>
        </span>
        <img class="detail__img" src={product ? product.img : null} alt="Product IMG" />
      </div>
      <div className="detail__rightContent">
        <div className="detail__header">
          <span class="detail__name">
            <img src="/images/point.png" class="point" />
            {product ? product.name : null}
          </span>
          <span class="detail__brand"></span>
        </div>
        <div class="detail__price">
          <span>가격 {product ? product.price : null}원</span>
        </div>
        <div class="detail__description">
          <div class="description__content">
            <span>상품설명</span>
            <span>{product ? product.description : null}</span>
          </div>
          <div class="detail__tagBox">
            <div class="detail__tag">
              <span>
                <span>연관태그</span>
                <form method="get" action="">
                  #<input type='submit' name='q' value="태그있는척"></input>
                </form>
              </span>
            </div>
            <div class="detail__tag--heart">
              <i class="fas fa-heart"></i>
              <span id='like-count'>{product ? product.like.length : null}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
};

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
      <DetailBox product={productDetail} />
    </main>
  );
};

export default Detail;
