Summary: Convert DLG Pro BBS message bases to HTML
Name: dlg2html
Version: 1.1
Release: 0
License: GPL-2.0+
Group: Applications/Text
URL: https://logological.org/%{name}
Source0: https://files.nothingisreal.com/software/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Prefix: %{_prefix}
Requires: bash, coreutils, sed, grep
BuildArch: noarch

%description
dlg2html is a set of Bash shell scripts which help automate the
conversion of DLG Pro message bases to HTML for archiving or mirroring
on the Web. (DLG Pro is a bulletin board system, or BBS, for Amiga
personal computers.) The HTML message files contain the appropriate
links to the next and previous messages, as well as to any replies or
referenced messages; a message index is also produced. dlg2html works
with terminal dumps of DLG message boards, which means you do not need
access to the actual BBS files to perform the conversion.

%prep
%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%{__install} -D dlg2html %{buildroot}%{_bindir}/dlg2html
%{__install} -D dlgsplit %{buildroot}%{_bindir}/dlgsplit

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/dlg2html
%{_bindir}/dlgsplit
%doc AUTHORS COPYING NEWS README example.txt

%changelog
* Mon Dec 26 2016 Tristan Miller <psychonaut@nothingisreal.com> - 
- Clean up RPM for OBS.
- Update URLs.
- Update license header per SPDX Specification.

* Sun Oct 13 2013 Tristan Miller <psychonaut@nothingisreal.com> - 
- Initial build.
