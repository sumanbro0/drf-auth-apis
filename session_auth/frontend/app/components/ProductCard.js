// ProductCard.js

import Image from "next/image";

const ProductCard = ({ name, description, price, product_image }) => {
    return (
        <div className="bg-white rounded-lg shadow-md p-4">
            <Image
                src={product_image[0].image}
                width={300} // Assuming only the first image for preview
                height={300} // Assuming only the first image for preview
                alt={name}
                className="w-full rounded-md mb-2"
            />
            <h2 className="text-xl font-semibold mb-2">{name}</h2>
            <p className="text-gray-600 mb-4">{description}</p>
            <p className="text-lg font-semibold text-blue-600">${price}</p>
        </div>
    );
};

export default ProductCard;
