<form method="POST" novalidate>
  <div class="mb-3">
    <label for="nameInput" class="form-label" >User Name</label>
    <input data-test="name-input" required name="name" type="text" class="form-control" id="nameInput" aria-describedby="nameHelp">
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input data-test="password-input" required name="password" type="password" class="form-control" id="exampleInputPassword1">
  </div>

  <button data-test="register-button" formaction="?/register" type="submit" class="btn btn-primary">Register</button>
  <button data-test="login-button" formaction="?/login" type="submit" class="btn btn-primary">Login</button>
</form>