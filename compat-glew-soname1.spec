#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-glew-soname1
Version  : 1.13.0
Release  : 14
URL      : http://downloads.sourceforge.net/project/glew/glew/1.13.0/glew-1.13.0.tgz
Source0  : http://downloads.sourceforge.net/project/glew/glew/1.13.0/glew-1.13.0.tgz
Summary  : The OpenGL Extension Wrangler library
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: compat-glew-soname1-lib
BuildRequires : cmake
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(x11)

%description
GLEW - The OpenGL Extension Wrangler Library
http://glew.sourceforge.net/
https://github.com/nigels-com/glew

%package dev
Summary: dev components for the compat-glew-soname1 package.
Group: Development
Requires: compat-glew-soname1-lib
Provides: compat-glew-soname1-devel

%description dev
dev components for the compat-glew-soname1 package.


%package lib
Summary: lib components for the compat-glew-soname1 package.
Group: Libraries

%description lib
lib components for the compat-glew-soname1 package.


%prep
%setup -q -n glew-1.13.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1500492328
pushd ./
make V=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1500492328
rm -rf %{buildroot}
pushd ./
%make_install
popd
## make_install_append content
mkdir -p %{buildroot}/usr/lib64/pkgconfig
cat > %{buildroot}/usr/lib64/pkgconfig/compat-glew1.pc << EOF
prefix=/usr
exec_prefix=${prefix}
libdir=/usr/lib64
includedir=${prefix}/include
Name: compat-glew1
Description: The OpenGL Extension Wrangler library
Version: 1.13.0
Cflags: -I${includedir}
Libs: -L${libdir} -lcompat-glew1
Requires: glu
EOF
ln -s libGLEW.so.1.13 %{buildroot}/usr/lib64/libcompat-glew1.so
## make_install_append end

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/GL/glew.h
%exclude /usr/include/GL/glxew.h
%exclude /usr/include/GL/wglew.h
%exclude /usr/lib64/libGLEW.so
%exclude /usr/lib64/pkgconfig/glew.pc
/usr/lib64/libcompat-glew1.so
/usr/lib64/pkgconfig/compat-glew1.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libGLEW.so.1.13
/usr/lib64/libGLEW.so.1.13.0
