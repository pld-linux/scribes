Summary:	Simple, slim and sleek text editor
Summary(pl.UTF-8):	Prosty, niewielki i elegancki edytor tekstu
Name:		scribes
Version:	0.3.3.3
Release:	4
License:	GPL
Group:		Applications/Editors
Source0:	http://downloads.sourceforge.net/scribes/%{name}-%{version}.tar.bz2
# Source0-md5:	1290e669550d3392791f1a21662939ee
URL:		http://scribes.sourceforge.net/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	python-dbus
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-gnome-desktop-gtksourceview
BuildRequires:	python-gnome-extras-gtkspell
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.5
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
%pyrequires_eq	python-modules
Requires:	python-gnome-desktop-gtksourceview
Requires:	python-gnome-desktop-print
Requires:	python-gnome-extras-gtkspell
Requires:	python-gnome-ui >= 2.12.2-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scribes is a simple and easy to use text editor for GNOME.

%description -l pl.UTF-8
Scribes jest jest prostym i łatwym w użyciu edytorem tekstu dla GNOME.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%{configure}
%{__make} \
	CC="%{__cc}" \
	PREFIX=%{_prefix} \
	LIBDIR=/%{_lib}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas

%{__make} install \
	PREFIX=%{_prefix} \
	LIBDIR=/%{_lib} \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/application-registry
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/SCRIBES/*.py

install data/scribes.schemas $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install scribes.schemas
%update_desktop_database_post
%scrollkeeper_update_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall scribes.schemas

%postun
%update_desktop_database_postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO TRANSLATORS
%attr(755,root,root) %{_bindir}/scribes
%dir %{py_sitescriptdir}/SCRIBES
%{py_sitescriptdir}/SCRIBES/*.py[co]
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_pixmapsdir}/scribes.png
%{_omf_dest_dir}/%{name}
%{_sysconfdir}/gconf/schemas/scribes.schemas
