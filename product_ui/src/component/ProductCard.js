import React from "react";

const ProductCard = ({ product }) => {
  return (
    <div className="product-card">
      <img src={product.image} alt={product.title} />
      <div className="product-info">
        <h3>{product.title}</h3>
        <p className="category">{product.category}</p>
        <p className="price">{product.price}</p>
      </div>
    </div>
  );
};

export default ProductCard;
