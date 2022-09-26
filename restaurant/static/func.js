const auth = (form) => {
    let form_data = new FormData(form)
    let jdata = {'login':form_data.get('login'), 'password':form_data.get('password')}
    fetch('/login',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(jdata),
    }).then((response) => {
        if (response.status == 400) {
            alert("invalid data")
            return
        }
        if (response.status == 401) {
            alert("bad auth")
            return
        }
        window.location.href = "/"
    })
}

const reg = (form) => {
    let form_data = new FormData(form)
    if (form_data.get('password') != form_data.get('password2')) {
        alert("passwords doesn't match")
        return
    }
    let jdata = {'login':form_data.get('login'), 'password':form_data.get('password')}
    fetch('/register',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(jdata),
    }).then((response) => {
        if (response.status == 400) {
            alert("invalid data")
            return
        }
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