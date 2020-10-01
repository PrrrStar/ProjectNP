import React, { useState, useEffect } from 'react';
import axios from "axios";
import '../css/category.css';


const Category = () => {
  const [categories, setCategories] = useState([]);
  const [drop, setDrop] = useState();

  useEffect(() => {
    getCategories();
  }, []);

  const getCategories = async () => {
    const { data } = await axios.get('/api/product-categories/');
    setCategories(data);
  }

  const onClickCategory = event => {
    const children = document.querySelectorAll(".category__children");
    let name = event.target.getAttribute("value");
    if (event.target.getAttribute("drop") == "f") {
      for (var i = 0; i < children.length; i++) {
        if (name == children[i].getAttribute("value")) {
          children[i].style.display = "flex";
        }
        console.log(children[i]);
      }
      event.target.setAttribute("drop", "t")
    }
    else {
      for (var j = 0; j < children.length; j++) {
        if (name == children[j].getAttribute("value")) {
          children[j].style.display = "none";
        }
      }
      event.target.setAttribute("drop", "f")
    }
  }

  return (
    <>
      <div class="category">
        <div class="category__container">
          {categories.map(category => {
            if (category.parent) {
              return <div class="category__children" value={category.parent}><a
                href="">{category.name}</a></div>
            } else {
              return <div class="category__parent" value={category.id} drop="f" onClick={onClickCategory}>{category.name}</div>
            }
          })}
        </div>
      </div>
    </>
  );
};

export default Category;