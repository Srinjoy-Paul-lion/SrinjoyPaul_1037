import React from "react";
import products from "./data/products";
import ProductCard from "./components/ProductCard";
import "./App.css";

const App = () => {
  return (
    <div className="container">
      <h1 className="title">Product Listing</h1>

      <div className="product-grid">
        {products.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
};

export default App;
