function getCookie(name) {
    const cookieName = name + '=';
    return (document.cookie.split('; ').reduce((cookieValue, cookie) => {
        if (cookieValue) return cookieValue;
        if (cookie.startsWith(cookieName)) return decodeURIComponent(cookie.substring(cookieName.length));
        return null;
    }, null)) || null;
}

const csrftoken = getCookie('csrftoken');

export {csrftoken}