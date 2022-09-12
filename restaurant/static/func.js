const auth = (form) => {
    let form_data = new FormData(form)
    fetch('/login',{
        method: 'POST',
        body: form_data,
    }).then((response) => {
        if (response.status == 401) {
            alert("bad auth")
            return
        }
        window.location.href = "/"
    })
}

const reg = (form) => {
    let form_data = new FormData(form)
    fetch('/register',{
        method: 'POST',
        body: form_data,
    }).then((response) => {
        if (response.status == 403) {
            alert("user exists")
            return
        }
        window.location.href = "/"
    })
}

const logout = () => {
    fetch('/logout')
}