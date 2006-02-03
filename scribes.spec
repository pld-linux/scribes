Summary:	Simple, slim and sleek text editor
Summary(pl):	Prosty, niewielki i elegancki edytor tekstu
Name:		scribes
Version:	0.2.4
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	http://openusability.org/download.php/86/%{name}-%{version}.tar.gz
# Source0-md5:	e14aa68c45f7bb46f1786b82bd14a283
Patch0:		%{name}-setup.patch
Patch1:		%{name}-desktop.patch
URL:		http://scribes.sourceforge.net/
BuildRequires:	GConf2-devel
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	python-gnome-devel >= 2.6.0
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.5
%pyrequires_eq  python-modules
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires:	python-gnome-extras-gtksourceview
Requires:	python-gnome-extras-gtkspell
Requires:	python-gnome-extras-print
Requires:	python-gnome-ui >= 2.12.2-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scribes is a simple and easy to use text editor for GNOME.

%description -l pl
Scribes jest jest prostym i ³atwym w u¿yciu edytorem tekstu dla GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas

python setup.py install \
        --optimize=2 \
        --root $RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/application-registry
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/Scribes/*.py

install data/scribes.schemas $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install scribes.schemas
%update_desktop_database_post
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall scribes.schemas

%postun
%update_desktop_database_postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ARTISTS AUTHORS CHANGELOG README TODO TRANSLATORS
%attr(755,root,root) %{_bindir}/scribes
%{py_sitescriptdir}/Scribes/*.py[co]
%{_datadir}/%{name}

%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

%{_omf_dest_dir}/%{name}
%{_sysconfdir}/gconf/schemas/scribes.schemas
