var app = new Vue({
  el: '#app',
  data: {
    post_price: 'Post Price',
    proceeds: ''
  },
  methods: {
    getProceeds: function () {
      var post_price = parseInt(this.item_price)
      var revenue = (post_price - (post_price * 0.09) - (post_price * 0.029 + .3).toFixed(2))
      this.proceeds = "Estimated Proceeds: \$" + revenue
    }
  }
})