import cls from 'classnames';

function Button({
  children,
  className,
  prefix,
  suffix,
  htmlType = 'button',
  shape = 'default',
  block = false,
  disabled = false,
  type = 'primary',
  ...otherProps
}) {
  const classes = cls(
    'border rounded-md px-4 py-2 my-2 transition font-semibold duration-500 ease select-none focus:outline-none focus:shadow-outline',
    {
      'border-primary bg-primary text-white hover:bg-primary-600':
        type == 'primary',
      'border-secondary bg-secondary text-white hover:bg-secondary-500':
        type == 'success',
      'border-gray-200 bg-gray-200 text-gray-700': type == 'light',
    },
    {
      rounded: shape == 'default',
      'rounded-full': shape == 'rounded',
    },
    {
      'h-5 w-5': type == 'radio',
    },
    { 'w-full': block },

    className
  );

  return (
    <button
      disabled={disabled}
      className={classes}
      type={htmlType}
      {...otherProps}
    >
      {prefix && <span>{prefix}</span>}
      {children}
      {suffix && <span>{suffix}</span>}
    </button>
  );
}

export default Button;
