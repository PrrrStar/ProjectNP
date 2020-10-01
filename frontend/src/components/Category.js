import React, { useState, useEffect } from 'react';
import axios from "axios";
import '../css/category.css';

const Category = () => {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    getCategories();
  }, []);

  const getCategories = async () => {
    const { data } = await axios.get('/api/product-categories/');
    setCategories(data);
  }

  return (
    <>
      <div class="category">
        <div class="category__container">
          {categories.map(category => {
            if (category.parent) {
              return <div class="category__children" value="{category.parent}"><a
                href="">{category.name}</a></div>
            } else {
              return <div class="category__parent" value="{category.name}" drop="f">{category.name}</div>
            }
          })}
        </div>
      </div>
    </>
  );
};

export default Category;