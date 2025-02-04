<?php

$target_file = "test.pdf.php";

if (!strpos($target_file,".pdf")){
	echo "only pdf cv";
} else {
	echo("bypass success " . $target_file);
}


?>
