import cls from 'classnames';

function Input({
  id,
  placeholder,
  className,
  block = false,
  type = 'text',
  size = 'medium',
  disabled = false,
  ...otherProps
}) {
  const classes = cls(
    'rounded-md border border-gray-200 bg-white  text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md',
    { 'w-full': block },
    {
      'py-2 px-4 text-sm font-normal': size == 'small',
      'py-3 px-6 text-base font-medium': size == 'medium',
      'py-3 px-6 text-lg font-medium': size == 'large',
    },
    className
  );

  return (
    <input
      id={id}
      disabled={disabled}
      className={classes}
      placeholder={placeholder}
      type={type}
      {...otherProps}
    />
  );
}

export default Input;
