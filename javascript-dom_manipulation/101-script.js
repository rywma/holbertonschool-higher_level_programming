document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('#btn_translate').addEventListener('click', () => {
    const languageCode = document.querySelector('#language_code').value;

    fetch(`https://hellosalut.stefanbohacek.com/?lang=${languageCode}`)
      .then((response) => response.json())
      .then((data) => {
        document.querySelector('#hello').textContent = data.hello;
      })
      .catch((error) => {
        console.error(error);
      });
  });
});