$('#slider1, #slider2, #slider3').owlCarousel({
  loop: true,
  margin: 20,
  responsiveClass: true,
  responsive: {
      0: {
          items: 1,
          nav: false,
          autoplay: true,
      },
      600: {
          items: 3,
          nav: true,
          autoplay: true,
      },
      1000: {
          items: 4,
          nav: true,
          loop: true,
          autoplay: true,
      }
  }
})


// cart + - button
// Path: nutranta\nutranta_app\templates\nutranta_app\cart.html
$('.plus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    // console.log(id);
    $.ajax({    
        type: "GET",
        url: "/pluscart",
        data:{
            prod_id: id
        },
        success: function(data){
            eml.innerText = data.quantity
            document.getElementById("amount").innerHTML = data.amount
            document.getElementById("totalamount").innerHTML = data.totalamount
            document.getElementById('cal').innerHTML = data.cal
            // document.getElementById("amount").innerHTML = data.amount
            // document.getElementById("totalamount").innerHTML = data.totalamount
        }
    })
    }
);

$('.minus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    // console.log(id);
    $.ajax({    
        type: "GET",
        url: "/minuscart",
        data:{
            prod_id: id
        },
        success: function(data){
            eml.innerText = data.quantity
            document.getElementById("amount").innerHTML = data.amount
            document.getElementById("totalamount").innerHTML = data.totalamount
            document.getElementById('cal').innerHTML = data.cal
            // document.getElementById("amount").innerHTML = data.amount
            // document.getElementById("totalamount").innerHTML = data.totalamount
        }
    })
    }
);

$('.remove-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this
    // console.log(id);
    $.ajax({    
        type: "GET",
        url: "/removecart",
        data:{
            prod_id: id
        },
        success: function(data){
            document.getElementById("amount").innerHTML = data.amount
            document.getElementById("totalamount").innerHTML = data.totalamount
            document.getElementById('cal').innerHTML = data.cal
            eml.parentNode.parentNode.parentNode.parentNode.remove()
            // document.getElementById("amount").innerHTML = data.amount
            // document.getElementById("totalamount").innerHTML = data.totalamount
        }
    })
    }
);

// cart counter
