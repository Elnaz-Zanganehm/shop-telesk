// // cart
// let cartIcon = document.querySelector('#basket-icon')
// let cart = document.querySelector('.cart')
// let closeCart = document.querySelector ('#close-cart')
// // open cart
// cartIcon.onclick = () => {
//     cart.classList.add('active')
// }
// // close cart
// closeCart.onclick = () => {
//     cart.classList.remove('active')
// }
//
// // Cart Working Js
// if(document.readyState == 'loading'){
//     document.addEventListener('DOMContentLoaded' , ready)
// }else {
//     ready();
// }
//
// // Making Function
// function ready(){
//     // remove item from cart
//     var removeCartButtons = document.getElementsByClassName('cart-remove')
//     console.log(removeCartButtons);
//     for (var i = 0; i < removeCartButtons.length; i++){
//         var button = removeCartButtons[i]
//         button.addEventListener('click' , removeCartItem)
//     }
//     // quantity changes
//     quantityInputs = document.getElementsByClassName('cart-quantity')
//     for (var i = 0; i < quantityInputs.length; i++) {
//         var input = quantityInputs[i]
//         input.addEventListener('change' , quantityChanged)
//     }
//     // add to cart
//     var addcart = document.getElementsByClassName('add-to-basket')
//     for (var i = 0; i < addcart.length; i++) {
//         var button = addcart[i]
//         button.addEventListener('click' , addcartClicked);
//     }
//     // buy button work
//     document.getElementsByClassName('btn-buy')[0].addEventListener('click' , buyButtonClicked);
// }
//
// // buy button
// function buyButtonClicked(){
//     alert('salam')
//     var cartContent = document.getElementsByClassName('cart-content')[0]
//     while (cartContent.hasChildNodes()){
//         cartContent.removeChild(cartContent.firstChild);
//     }
//     updatetotal();
// }
//
// // remove item from cart
// function removeCartItem(e){
//     var buttonClicked = e.target
//     buttonClicked.parentElement.remove()
//     updatetotal();
// }
//
// // quantity changes
// function quantityChanged (e) {
//     var input = e.target
//     if (isNaN(input.value) || input.value <= 0 ) {
//         input.value = 1
//     }
//     updatetotal()
// }
// // add to cart
// function addcartClicked(e){
//     var button = e.target
//     var shopProducts = button.parentElement
//     var title = shopProducts.getElementsByClassName('product-title')[0].innerText
//     var price = shopProducts.getElementsByClassName('price')[0].innerText
//     var productImg = shopProducts.getElementsByClassName('product-img')[0].src;
//     addProductToCart(title , price , productImg);
//     updatetotal()
// }
//
// // function addProductToCart(title , price , productImg){
// //     var cartShopBox = document.createElement('div');
//
// //     cartShopBox.classList.add('cart-box');
//
// //     var cartItems = document.getElementsByClassName('cart-content')[0];
// //     var cartItemsNames = cartItems.getElementsByClassName('cart-product-title');
// //     for (var i = 0; i < cartItemsNames.length; i++) {
// //         alert('شما قبلا این محصول را به سبد خرید خود اضافه کردید');
// //         return;
// //     }
//
// // }
//
// // var cartBoxContent = `
// //                         <img src="./img/m01.jpg" alt="" class="cart-img p-1">
// //                         <div class="detail-box">
// //                             <div class="cart-product-title">هودی</div>
// //                             <div class="cart-price">260000تومان</div>
// //                             <input type="number" value="1" class="cart-quantity">
// //                         </div>
// //                         <!-- remove cart-->
// //                         <i class="bi bi-x-circle-fill cart-remove"></i>` ;
//
// // cartShopBox.innerHTML = cartBoxContent;
// // cartItems.append(cartShopBox);
// // cartShopBox.getElementsByClassName('cart-remove')[0].addEventListener('click' , removeCartItem);cartShopBox.getElementsByClassName('cart-quantity')[0].addEventListener('change' , quantityChanged);
//
// function addProductToCart(title, price, productImg) {
//     var cartBoxContent =
//         `<img src="${productImg}" alt="" class="cart-img p-1">
//         <div class="detail-box">
//             <div class="cart-product-title">${title}</div>
//             <div class="cart-price">${price}</div>
//             <input type="number" value="1" class="cart-quantity">
//         </div>
//         <i class="bi bi-x-circle-fill cart-remove"></i>`;
//
//     var cartShopBox = document.createElement('div');
//     cartShopBox.classList.add('cart-box');
//     cartShopBox.innerHTML = cartBoxContent;
//
//     var cartItems = document.getElementsByClassName('cart-content')[0];
//     var cartItemsNames = cartItems.getElementsByClassName('cart-product-title');
//     for (var i = 0; i < cartItemsNames.length; i++) {
//         alert('شما قبلا این محصول را به سبد خرید خود اضافه کردید');
//         return;
//     }
//     cartItems.appendChild(cartShopBox);
//
//     cartShopBox.getElementsByClassName('cart-remove')[0].addEventListener('click', removeCartItem);
//     cartShopBox.getElementsByClassName('cart-quantity')[0].addEventListener('change', quantityChanged);
//
// }
//
// // update total
// function updatetotal(){
//     var cartContent = document.getElementsByClassName('cart-content')[0];
//     var cartBoxes = cartContent.getElementsByClassName('cart-box');
//     var total = 0;
//
//
//     for (var i = 0; i < cartBoxes.length; i++){
//        var cartBox =cartBoxes[i];
//        console.log(cartBox);
//     //    var priceElement = cartBox.getElementsByTagName('cart-price')[0];
//        var priceElement = cartBox.children[1].children[1]
//     //    var quantityElement = cartBox.getElementsByClassName('cart-quantity')[0];
//        var quantityElement = cartBox.children[1].children[2]
//     //    var price = parseFloat(priceElement.innerText.replase("تومان" , " "));
//        var price = priceElement.innerText.replace("تومان" , " ");
//
//        var quantity = quantityElement.value;
//        total = total + (price * quantity);
//     }
//     //if price contain some cents value
//     total= Math.round(total * 100) / 100 ;
//     document.getElementsByClassName('total-price')[0].innerText = 'تومان' + total;
//
// }