echo -n 'test' | sha256sum
echo -n 'test<SALT-A>' | sha256sum
echo -n 'test<SALT-B>' | sha256sum
