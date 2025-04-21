%global commit c674db53d9f092b0227d24aed58ef5f37ad53a71
%global shortcommit c674db5

Name:		virglrenderer
Version:	1.1.2
Release:	1.git%{shortcommit}%{?dist}

Summary:	Virgl Rendering library.
License:	MIT

# Use a different URL format that works with GitLab
Source:		https://gitlab.freedesktop.org/virgl/virglrenderer/-/archive/%{commit}/virglrenderer-%{commit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:	libepoxy-devel
BuildRequires:	mesa-libgbm-devel
BuildRequires:	mesa-libEGL-devel
BuildRequires:	python3
BuildRequires:	libdrm-devel
BuildRequires:  libva-devel
BuildRequires:  vulkan-loader-devel
BuildRequires:  python3-pyyaml

%description
The virgil3d rendering library is a library used by
qemu to implement 3D GPU support for the virtio GPU.

%package devel
Summary: Virgil3D renderer development files

Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Virgil3D renderer development files, used by
qemu to build against.

%package test-server
Summary: Virgil3D renderer testing server

Requires: %{name}%{?_isa} = %{version}-%{release}

%description test-server
Virgil3D renderer testing server is a server
that can be used along with the mesa virgl
driver to test virgl rendering without GL.

%prep
%autosetup -p1

%build
%meson -Dvideo=true -Dvenus=true
%meson_build

%install
%meson_install

%files
%license COPYING
%{_libdir}/libvirglrenderer.so.1{,.*}
%{_libexecdir}/virgl_render_server

%files devel
%dir %{_includedir}/virgl/
%{_includedir}/virgl/*
%{_libdir}/libvirglrenderer.so
%{_libdir}/pkgconfig/virglrenderer.pc

%files test-server
%{_bindir}/virgl_test_server

%changelog
