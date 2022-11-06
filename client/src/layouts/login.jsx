function LoginLayout({ children }) {
  return (
    <div className="flex h-screen">
      {/* <div className="w-7/12 px-6 py-12 bg-blue-900">BG</div> */}
      <div className="mx-auto w-5/12 px-6 py-12 flex flex-col justify-center">
        {children}
      </div>
    </div>
  );
}

export default LoginLayout;
