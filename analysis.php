<!DOCTYPE html>
<html lang="en" >
<?php
include_once "header.php";
?>
<html>
<body>
<center><hr style="width:70%"></center>
<br><br><br><br>
    <form>
        <h1>NIMBUS 2000</h1>
        <br>
        <label for="file"></label>
        <input  type="file" id="myFile" name="filename">
        <br>
        <select name="select" id="select">
          <option value="kmeans">K-Menas</option>
          <option value="birch">Birch</option>
        </select>
        <br>
        <button type="submit">Analyze</button>
      </form>

<script src='https://www.marcoguglie.it/Codepen/AnimatedHeaderBg/demo-1/js/EasePack.min.js'></script>
<script src='https://www.marcoguglie.it/Codepen/AnimatedHeaderBg/demo-1/js/rAF.js'></script>
<script src='https://www.marcoguglie.it/Codepen/AnimatedHeaderBg/demo-1/js/TweenLite.min.js'></script>
<script  src="./script.js"></script>

</body>
</html>

