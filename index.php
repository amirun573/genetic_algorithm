<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
<?php
// define variables and set to empty values
$initial = $n_solution = $n_children = $n_best = $n_iteration = "";

if (isset($_GET['submit'])) {
  $initial = test_input($_GET["initial"]);
  $n_solution = test_input($_GET["n_solution"]);
  $n_children = test_input($_GET["n_children"]);
  $n_best = test_input($_GET["n_best"]);
  $n_iteration = test_input($_GET["n_iteration"]);


  $output = shell_exec("python terengganu.py $initial $n_solution $n_children $n_best $n_iteration");

}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

?>
<html>
  <head>
    <title>Terengganu Road Plan</title>
    <style>
    .myForm {
    font-family: "Lucida Sans Unicode", "Lucida Grande", sans-serif;
    font-size: 0.8em;
    width: 20em;
    padding: 1em;
    border: 1px solid #ccc;
    }

    .myForm * {
    box-sizing: border-box;
    }

    .myForm fieldset {
    border: none;
    padding: 0;
    }

    .myForm legend,
    .myForm label {
    padding: 0;
    font-weight: bold;
    }

    .myForm label.choice {
    font-size: 0.9em;
    font-weight: normal;
    }
    .output-section{
      text-align: center;
    }

    .myForm input[type="text"],
    .myForm input[type="tel"],
    .myForm input[type="email"],
    .myForm input[type="datetime-local"],
    .myForm select,
    .myForm textarea {
    display: block;
    width: 100%;
    border: 1px solid #ccc;
    font-family: "Lucida Sans Unicode", "Lucida Grande", sans-serif;
    font-size: 0.9em;
    padding: 0.3em;
    }

    .myForm textarea {
    height: 100px;
    }

    .myForm button {
    padding: 1em;
    border-radius: 0.5em;
    background: #eee;
    border: none;
    font-weight: bold;
    margin-top: 1em;
    }

    .myForm button:hover {
    background: #ccc;
    cursor: pointer;
    }
    </style>
  </head>
  <body style="margin:0px;background:white;">
    <h2 style="text-align: center;background: yellow;margin:0px;padding-top:10px;padding-bottom:10px;">Terengganu Road Plan</h2>
    <br>
    <br>
    <div class="wrapper" style="displaY:flex;">
      <div class="input-section" style="width:auto;border:1px solid black;background:grey;">
        <form class="myForm" method="get" action="<?=$_SERVER['PHP_SELF'];?>">
          <p>
          <label>Initial Population
          <input type="text" class="form-control" name="initial" value="15" required>
          </label>
          </p>

          <p>
          <label>Number of Solutions each Iteration
          <input type="text" class="form-control" name="n_solution" value="10" required>
          </label>
          </p>

          <p>
          <label>Number of Children each iteration
          <input type="text" class="form-control" name="n_children" value="6" required>
          </label>
          </p>

          <p>
          <label>Number of Best solution from previous generation each iteration
          <input type="text" class="form-control" name="n_best" value="4" required>
          </label>
          </p>

          <p>
          <label>Number of iteration
          <input type="text" class="form-control" name="n_iteration" value="100" required>
          </label>
          </p>

          <p><input type="submit" class="btn btn-primary" name="submit" value="submit"/></p>

        </form>
      </div>
      <div class="output-section" style="width:100%;background:#e0e2e5;">
        <?php
        if (isset($_GET['submit'])) {
          echo $output;
        }
         ?>
      </div>
    </div>

  </body>
</html>
