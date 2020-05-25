<!DOCTYPE html>
<html>

  <head>
    <title>
      My Portfolio
    </title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, 
        initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="bootstrap/bootstrap.min.css">
    <script src="bootstrap/jquery.min.js"></script>
    <script src="bootstrap/popper.min.js"></script>
    <script src="bootstrap/bootstrap.min.js"></script>
    <style>
      /*  body {

        background-image: url("static/115.JPG");
        
      }*/

      .a {
        background-color: black;
        padding: 20px;

      }

      .b {
        padding-left: 10px;
        padding-right: 80px;
        color: white;
      }


      .container {
        margin-left: 0px;
        margin-right: 0px;
      }

      body,
      html {
        height: 100%;
        margin: 0;
        font-family: Arial, Helvetica, sans-serif;
      }

      * {
        box-sizing: border-box;
      }

      .bg-image {
        /* The image used */
        background-image: url("static/115.JPG");

        /* Add the blur effect */
        filter: blur(8px);
        -webkit-filter: blur(1px);

        /* Full height */
        height: 100%;

        /* Center and scale the image nicely */
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
      }

      /* Position text in the middle of the page/image */

      .bg-text {
        background-color: rgb(0, 0, 0);
        /* Fallback color */
        background-color: rgba(0, 0, 0, 0.4);
        /* Black w/opacity/see-through */
        color: white;
        font-weight: bold;
        border: 3px solid #f1f1f1;
        position: absolute;
        top: 80%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 2;
        width: 80%;
        padding: 20px;
        text-align: center;
      }

      @media (max-width:768px) {
        .bg-image {
          /* The image used */
          background-image: url("static/115.JPG");

          /* Add the blur effect */
          filter: blur(8px);
          -webkit-filter: blur(1px);

          /* Full height */
          height: 100%;
          width: 100%;

          /* Center and scale the image nicely */
          background-position: center;
          background-repeat: no-repeat;
          background-size: cover;
        }


        .bg-text {
          background-color: rgb(0, 0, 0);
          /* Fallback color */
          background-color: rgba(0, 0, 0, 0.4);
          /* Black w/opacity/see-through */
          color: white;
          font-weight: bold;
          border: 3px solid #f1f1f1;
          position: absolute;
          top: 70%;
          left: 50%;
          transform: translate(-50%, -50%);
          z-index: 2;
          width: 80%;
          padding: 0px;
          text-align: center;
        }

      }
    </style>
  </head>

  <body>
    <div class="row">
      <div class="col-12 a">
        <a class="b" href="https://tap.ibhubs.in/2019/harshitha-guttula/me.html">About me</a>
        <a class="b" href="https://tap.ibhubs.in/2019/harshitha-guttula/qualifications.html">Qualifications</a>
        <a class="b" href="https://tap.ibhubs.in/2019/harshitha-guttula/skills.html">Skills</a>
        <a class="b" href="https://tap.ibhubs.in/2019/harshitha-guttula/hobbies.html">Hobbies</a>
        <a class="b" href="#">Achievements</a>
        <a class="b" href="#">Contact</a>
      </div>
    </div>
    <div class="bg-image"></div>
    <div class="bg-text h">
      <h1 style="font-size:50px">I am Harshitha Guttula</h1>
      <p>And I'm the Designer of my life</p>
    </div>

  </body>

</html>
