var map;
      function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: 37.4525268, lng: 127.1326255},
          zoom: 15
        });

        var marker = new google.maps.Marker({
            position : {lat: 37.4525268, lng: 127.1326255},
            map:map,
            label: {text: "복지관", color:'black', fontSize:'20px'},
            title:'가천대'
        });
      }