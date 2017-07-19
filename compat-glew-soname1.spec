#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-glew-soname1
Version  : 1.13.0
Release  : 12
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
export SOURCE_DATE_EPOCH=1500401023
pushd ./
make V=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1500401023
rm -rf %{buildroot}
pushd ./
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/GL/glew.h
%exclude /usr/include/GL/glxew.h
%exclude /usr/include/GL/wglew.h
%exclude /usr/lib64/libGLEW.so
%exclude /usr/lib64/pkgconfig/glew.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libGLEW.so.1.13
/usr/lib64/libGLEW.so.1.13.0
