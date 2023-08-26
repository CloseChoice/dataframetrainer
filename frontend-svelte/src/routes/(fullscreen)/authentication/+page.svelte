<script>
  /** @type {import('./$types').PageData} */    export let data;
  /** @type {import('./$types').ActionData} */    export let form;


  
</script>

<form method="POST" novalidate>
  <div class="mb-3">
    <label for="nameInput" class="form-label" >User Name</label>
    <input 
      class:is-invalid={form?.username?.isValid === false} 
      class:is-valid={form?.username?.isValid === true} 
      data-test="name-input" required name="name" type="text" class="form-control" id="nameInput" aria-describedby="nameHelp">
    <div class="invalid-feedback" >
      {form?.username?.feedback}
    </div>
    <div>

    </div>
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input 
    class:is-invalid={form?.password?.isValid === false} 
    class:is-valid={form?.password?.isValid === true} 
    data-test="password-input" required name="password" type="password" class="form-control" id="exampleInputPassword1">
    <div class="invalid-feedback">
      {form?.password?.feedback}
    </div>
  
  </div>

  <button data-test="register-button" formaction="?/register" type="submit" class="btn btn-primary">Register</button>
  <button data-test="login-button" formaction="?/login" type="submit" class="btn btn-primary">Login</button>
</form>