import cls from 'classnames';

function FileUpload({ className, size = 'default' }) {
  const classes = cls(
    'mx-auto',
    {
      'w-4 h-4': size == 'default',
      'w-24 h-24': size == 'large',
    },
    className
  );

  return (
    <svg
      className={classes}
      viewBox="0 0 32 32"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path d="M 6 3 L 6 29 L 26 29 L 26 9.5996094 L 25.699219 9.3007812 L 19.699219 3.3007812 L 19.400391 3 L 6 3 z M 8 5 L 18 5 L 18 11 L 24 11 L 24 27 L 8 27 L 8 5 z M 20 6.4003906 L 22.599609 9 L 20 9 L 20 6.4003906 z M 16 13 L 12 17 L 15 17 L 15 22 L 17 22 L 17 17 L 20 17 L 16 13 z M 12 23 L 12 25 L 20 25 L 20 23 L 12 23 z" />
    </svg>
  );
}

export default FileUpload;
