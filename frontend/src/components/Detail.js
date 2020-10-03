import React from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const Detail = () => {
  let { slug } = useParams();
  const getProduct = async () => {
    const { data } = await axios.get("/api/products/" + { slug });
  };

  return <></>;
};

export default Detail;
