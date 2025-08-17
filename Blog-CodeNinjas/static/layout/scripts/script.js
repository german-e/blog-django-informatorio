//Funcion javascript para darle al boton like sin recargar la página

document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.btn-like').forEach(btn => {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      const postId = this.dataset.id;

      const url = this.dataset.url;
      console.log('Se hizo clic en el boton con url: ', url);

      //anterior: fetch(blog/posts/${postId}/like/

      fetch(url, {
        method: 'POST',
        headers: {
          'X-CSRFToken': getCookie('csrftoken'),
          'X-Requested-With': 'XMLHttpRequest',
        }
      })
      .then(response => response.json())
      .then(data => {
        const container = document.getElementById(`like-container-${postId}`);
        const icon = container.querySelector('i');
        const count = container.querySelector('.like-count');

        if (data.dio_like) {
          icon.className = 'fas fa-heart';
        } else {
          icon.className = 'far fa-heart';
        }
        count.textContent = data.likes;
      });
    });
  });
});

// Función para obtener CSRF token de la cookie
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}