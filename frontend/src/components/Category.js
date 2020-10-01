import React, { useState, useEffect } from 'react';
import axios from "axios";

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
          {categories.map(category => (
            <div>{category.name}</div>
          ))}
        </div>
      </div>
    </>
  );
};

export default Category;