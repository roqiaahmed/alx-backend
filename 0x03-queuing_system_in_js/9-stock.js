const express = require("express");
const kue = require("kue");

const app = express();

const listProducts = [
  { Id: 1, name: "Suitcase 250", price: 50, stock: 4 },
  { Id: 2, name: "Suitcase 450", price: 100, stock: 10 },
  { Id: 3, name: "Suitcase 650", price: 350, stock: 2 },
  { Id: 4, name: "Suitcase 1050", price: 550, stock: 5 },
];

function getItemById(id) {
  const product = listProducts.find((item) => item.Id === id);
  if (!product) {
    return;
  }

  return product;
}

app.get("/list_products", (req, res) => {
  console.log(`===============================> id is   `);
  return res.json(listProducts);
});

app.get("/list_products/:itemId", (req, res) => {
  const itemId = Number(req.params.itemId);

  const product = getItemById(itemId);
  console.log(`===========> ${product}`);
  if (!product) {
    return res.status(404).send({ status: "Product not found" });
  }
  res.status(201).json(product);
});

app.listen(1245, () => {
  console.log("run the server in port 1245 ....");
});
