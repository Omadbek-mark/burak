import mongoose, { Schema } from "mongoose";
import { ProductCollection, ProductSize, ProductStatus, ProductVolume } from "../libs/enums/product.enum";

const productSchema = new Schema(
  {
    productStatus: {
      type: String,
      enum: ProductStatus,
      default: ProductStatus.PAUSE
    },

    ProductCollection: {
      type: String,
      enum: ProductStatus,
      required: true,
    },

    ProductName: {
      type: String,
      required: true,
    },

    ProductPrice: {
      type: Number,
      required: true,
    },

    ProductLeftCount: {
      type: Number,
      required: true,
    },

    ProductSize: {
      type: String,
      enum: ProductSize,
      default: ProductSize.NORMAL
    },

    ProductVolume: {
      type: String,
      enum: ProductVolume,
      default: ProductVolume.ONE
    },

    productDesc: {
      type: String,
      required: true,
    },

    productImages: {
      type: [String],
      default: [],
    },

    productViews: {
      type: Number,
      default: 0,
    },
  },
  { timestamps: true }  // updatedAt, createdAt
);

productSchema.index(
  { productName: 1, productSize: 1, ProductVolume: 1 },
  { unique: true }
);
export default mongoose.model("Product", productSchema);