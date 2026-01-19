import React from "react";
import products from "./data/products";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Product Listing</h1>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))", gap: "20px" }}>
        {products.map((product) => (
          <div key={product.id} style={{ border: "1px solid #ddd", padding: "15px", borderRadius: "8px" }}>
            <img src={product.image} alt={product.title} style={{ width: "100%" }} />
            <h3>{product.title}</h3>
            <p>₹{product.price}</p>
            <p>{product.category}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
