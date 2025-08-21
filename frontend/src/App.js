import React, { useState } from "react";
import ProductList from "./components/ProductList";
import { Search, User, ShoppingCart, X } from "lucide-react";

function App() {
  const [showSearch, setShowSearch] = useState(false);

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-md">
        <div className="container mx-auto px-6 py-4 flex justify-between items-center">
          {/* Logo / Shop Name */}
          <h1 className="text-2xl font-bold text-gray-800">
            La Casita Online
          </h1>

          {/* Right Side Icons */}
          <div className="flex items-center space-x-6">
            {/* Search */}
            <div className="relative">
              {showSearch ? (
                <div className="flex items-center space-x-2">
                  <input
                    type="text"
                    placeholder="Buscar productos ..."
                    className="border border-gray-300 rounded-lg px-3 py-1 focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                  <button
                    className="text-gray-600 hover:text-red-500"
                    onClick={() => setShowSearch(false)}
                  >
                    <X className="w-5 h-5" />
                  </button>
                </div>
              ) : (
                <button
                  className="text-gray-600 hover:text-blue-500"
                  onClick={() => setShowSearch(true)}
                >
                  <Search className="w-6 h-6" />
                </button>
              )}
            </div>

            {/* User */}
            <button className="text-gray-600 hover:text-blue-500">
              <User className="w-6 h-6" />
            </button>

            {/* Cart */}
            <button className="relative text-gray-600 hover:text-blue-500">
              <ShoppingCart className="w-6 h-6" />
              <span className="absolute -top-2 -right-2 bg-blue-500 text-white text-xs w-5 h-5 flex items-center justify-center rounded-full">
                0
              </span>
            </button>
          </div>
        </div>
      </header>

      {/* Body */}
      <main className="max-w-7xl mx-auto px-6 py-8">
        <h2 className="text-xl font-semibold mb-4">Productos</h2>
        <ProductList />
      </main>
    </div>
  );
}

export default App;
