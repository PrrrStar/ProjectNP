import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import "../css/detail.css";
import "../css/comment.css";

const Comment = ({ comments }) => {
  return (
    <>
      <span>{comments}</span>
    </>
  )
}

const CommentBox = ({ product }) => {
  const [comments, setComments] = useState([]);

  useEffect(() => {
    getComment();
  }, [product])

  const getComment = async () => {
    if (product) {
      const commentId = product.comments.map(comment => comment.split('/')[5]);
      const commentArray = []
      commentId.map(async id => {
        const { data } = await axios.get(`/api/comments/${id}`);
        commentArray.push(data);
      });
      setComments(commentArray);
    };
  };

  return (
    <div className="detail__comment">
      <div className="comment__header">
        <div className="comment__header--title">
          <img src="/images/point.png" className="point" alt="point" />
          상품후기({product ? product.comments.length : null}개)
        </div>
      </div>
      <div className="comment__comments">
        {comments ? comments.map((c) => <div>{c.id}</div>) : null}
      </div>
    </div >
  )
}

const DetailBox = ({ product }) => {
  return (
    <div className="detailBox">
      <div className="detail__leftContent">
        <span className="detail__title">
          {product ? product.category.first : null}
          <span> &gt; {product ? product.category.second : null}</span>
        </span>
        <img className="detail__img" src={product ? product.img : null} alt="Product IMG" />
      </div>
      <div className="detail__rightContent">
        <div className="detail__header">
          <span className="detail__name">
            <img src="/images/point.png" className="point" alt="point" />
            {product ? product.name : null}
          </span>
          <span className="detail__brand"></span>
        </div>
        <div className="detail__price">
          <span>가격 {product ? product.price : null}원</span>
        </div>
        <div className="detail__description">
          <div className="description__content">
            <span>상품설명</span>
            <span>{product ? product.description : null}</span>
          </div>
          <div className="detail__tagBox">
            <div className="detail__tag">
              <span>
                <span>연관태그</span>
                <form method="get" action="">
                  #<input type='submit' name='q' value="태그있는척"></input>
                </form>
              </span>
            </div>
            <div className="detail__tag--heart">
              <i className="fas fa-heart"></i>
              <span id='like-count'>{product ? product.like.length : null}</span>
            </div>
          </div>
        </div>
        <div className="detail__button">
          <button className="detail__stock">
            <span>재고확인</span>
            <img src="/images/location__white.png" alt="재고확인" />
          </button>
          <button type="button" className="detail__naeggu {% if user in product.like.all %}detail__naeggu__active{% endif %}" id='btn-like' data-url='{{ product.get_api_like_url }}' data-like='{{product.like.count}}'>
            <span>내꺼하기</span>
            <img src="/images/heart__white.png" alt="내꺼하기" />
          </button>
        </div>
      </div>
    </div>
  )
};

const Detail = () => {
  let { slug } = useParams();
  const [productDetail, setProductDetail] = useState();

  useEffect(() => {
    const getProduct = async () => {
      const { data } = await axios.get("/api/products/" + slug);
      setProductDetail(data);
    };

    getProduct();
  }, [slug]);

  return (
    <main className="detail">
      <DetailBox product={productDetail} />
      <CommentBox product={productDetail} />
    </main>
  );
};

export default Detail;
