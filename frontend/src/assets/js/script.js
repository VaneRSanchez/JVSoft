export const applyInputEffects = () => {
  const inputGroups = document.querySelectorAll('.input-group');

  inputGroups.forEach(inputGroup => {
    const input = inputGroup.querySelector('input');

    if (input.value.trim()) {
      inputGroup.classList.add('active');
    }

    input.addEventListener('focus', () => {
      inputGroup.classList.add('active');
    });

    input.addEventListener('blur', () => {
      if (!input.value.trim()) {
        inputGroup.classList.remove('active');
      }
    });

    input.addEventListener('input', () => {
      if (input.value.trim()) {
        inputGroup.classList.add('active');
      }
    });

    inputGroup.addEventListener('click', () => {
      input.focus();
    });
  });
};