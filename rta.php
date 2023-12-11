<?php 
$id=$_GET['id'];


if($id==1){
    $start = microtime(true);
    exec('python python/k-means.py');
    $end = microtime(true);
    $elapsed = $end - $start;
    echo"
    <center>
    <br>
    <h2 style='color:green'>K-Means Clustering | Execution Time:  $elapsed sec </h2><br/><br/>  
    <img src='clusters/kmeans.png'>
    </center>
    ";
}

if($id==2){
    $start = microtime(true);
    exec('python python/birch_1.py');
    $end = microtime(true);
    $elapsed = $end - $start;
    echo"
    <center>
    <h2 style='color:green'>Birch Clustering | Execution Time:  $elapsed sec </h2><br/><br/>  
    <img src='clusters/birch.png'>
    </center>
    ";
}

if($id==3){
    $start = microtime(true);
    exec('python python/DBSCAN_clustering.py');
    $end = microtime(true);
    $elapsed = $end - $start;
    echo"
    <center>
    <br>
    <h2 style='color:green'>DBSCAN Clustering | Execution Time:  $elapsed sec </h2><br/><br/>  
    <img src='clusters/DBSCAN.png'>
    </center>
    ";
}

if($id==4){
    $start = microtime(true);
    exec('python python\Gaussian_Mixture.py');
    $end = microtime(true);
    $elapsed = $end - $start;
    echo"
    <center>
    <h2 style='color:green'>Gaussian Mixture Clustering | Execution Time:  $elapsed sec </h2><br/><br/>  
    <img src='clusters/Gaussian.png'>
    </center>
    "; 
}

if($id==5){
    $start = microtime(true);
    exec('python python/Hierarchical_clustering.py');
    $end = microtime(true);
    $elapsed = $end - $start;
    echo"
    <center>
    <br>
    <h2 style='color:green'>Hierarchical clustering.py Clustering | Execution Time:  $elapsed sec </h2><br/><br/>  
    <img src='clusters/Hierarchical_clustering.png'>
    </center>
    ";
}

if($id==6){
    $start = microtime(true);
    exec('python python/mean_shift.py');
    $end = microtime(true);
    $elapsed = $end - $start;
    echo"
    <center>
    <br>
    <h2 style='color:green'>Mean Shift Clustering | Execution Time:  $elapsed sec </h2><br/><br/>  
    <img src='clusters/mean_shift.png'>
    </center>
    ";
}

if($id==7){
    $start = microtime(true);
    exec('python python/Optics_Clustering.py');
    $end = microtime(true);
    $elapsed = $end - $start;
    echo"
    <center>
    <br>
    <h2 style='color:green'>Optics Clustering  | Execution Time:  $elapsed sec </h2><br/><br/>  
    <img src='clusters/Optics_Clustering.png'>
    </center>
    ";
}

if($id==8){
    $start = microtime(true);
    exec('python python/Spectral_Clustering.py');
    $end = microtime(true);
    $elapsed = $end - $start;
    echo"
    <center>
    <br>
    <h2 style='color:green'>Spectral Clustering  | Execution Time:  $elapsed sec </h2><br/><br/>  
    <img src='clusters/Spectral_Clustering.png'>
    </center>
    ";
}

if($id==9){
    $start = microtime(true);
    exec('python python/Ward_Hierarchical.py');
    $end = microtime(true);
    $elapsed = $end - $start;
    echo"
    <center>
    <br>
    <h2 style='color:green'>Ward Hierarchical  | Execution Time:  $elapsed sec </h2><br/><br/>  
    <img src='clusters/Ward_Hierarchical.png'>
    </center>
    ";
}

if($id==10){
    $start = microtime(true);
    exec('python python/HDB_scan.py');
    $end = microtime(true);
    $elapsed = $end - $start;
    echo"
    <center>
    <br>
    <h2 style='color:green'>HDB  | Execution Time:  $elapsed sec </h2><br/><br/>  
    <img src='clusters/HDB.png'>
    </center>
    ";
}

if($id==11){
    $start = microtime(true);
    exec('python python/Affinity_Propagation.py');
    $end = microtime(true);
    $elapsed = $end - $start;
    echo"
    <center>
    <br>
    <h2 style='color:green'>Affinity Propagation | Execution Time:  $elapsed sec </h2><br/><br/>  
    <img src='clusters/Affinity.png'>
    </center>
    ";
}

if($id==12){
    $start = microtime(true);
    exec('python python/Bisecting k-means.py');
    $end = microtime(true);
    $elapsed = $end - $start;
    echo"
    <center>
    <br>
    <h2 style='color:green'>Bisecting k-means  | Execution Time:  $elapsed sec </h2><br/><br/>  
    <img src='clusters/Bisecting.png'>
    </center>
    ";
}
?>