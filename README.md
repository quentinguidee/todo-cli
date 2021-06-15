# todo-cli

A tool to manage the study of courses at the university.

## Status

- [x] Add/Remove/List Courses

![image](https://user-images.githubusercontent.com/12123721/121871890-ede98700-cd04-11eb-905e-0c0400facfb2.png)

- [x] Add/Remove/List course tasks (lab/chapter/session/course)

![image](https://user-images.githubusercontent.com/12123721/121872005-12456380-cd05-11eb-9429-6d5a53d0a523.png)

- [x] Change task status (not-done/almost-done/done)

![image](https://user-images.githubusercontent.com/12123721/121872097-2b4e1480-cd05-11eb-87e8-a8fabb23995b.png)

- [ ] Timers
- [ ] Today
- [ ] Documentation
- [ ] Autocomplete
- [x] Unit tests and E2E tests
- [ ] Errors handling

## Contributing

After `git clone`, run this script to install required packages and setup a git hook that runs tests and pycodestyle before each commit.

```bash
sh install-dev-tools.sh
```

### Run project

```bash
python3 main.py
```

### Manually run tests

```bash
python3 tests.py
```

### Manually run pycodestyle

```bash
pycodestyle . --max-line-length=120
```

## License

This project is released under the [MIT License](./LICENSE.md)
