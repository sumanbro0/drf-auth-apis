// ProductGrid.js

import ProductCard from './ProductCard';

const Products = async () => {
    const response = await fetch('http://127.0.0.1:8000/api/products', {
        method: 'GET',
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
    })
    const products = await response.json()

    return (
        <div className="m-10 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
            {products.map((product, index) => (
                <ProductCard key={index} {...product} />
            ))}
        </div>
    );
};

export default Products;
