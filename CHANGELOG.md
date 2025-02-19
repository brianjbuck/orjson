# Changelog

## 2.1.1 - 2019-10-29

### Changed

- Publish `manylinux1` wheels instead of `manylinux2010`.

## 2.1.0 - 2019-10-24

### Added

- `orjson.dumps()` serializes `dataclasses.dataclass` instances if
`option=orjson.OPT_SERIALIZE_DATACLASS` is specified.
- `orjson.dumps()` accepts `orjson.OPT_UTC_Z` to serialize UTC as "Z" instead
of "+00:00".
- `orjson.dumps()` accepts `orjson.OPT_OMIT_MICROSECONDS` to not serialize
the `microseconds` attribute of `datetime.datetime` and `datetime.time`
instances.
- `orjson.loads()` accepts `bytearray`.

### Changed

- Drop support for Python 3.5.
- Publish `manylinux2010` wheels instead of `manylinux1`.

## 2.0.11 - 2019-10-01

### Changed

- Publish Python 3.8 wheel for Linux.

## 2.0.10 - 2019-09-25

### Changed

- Performance improvements and lower memory usage in deserialization
by creating only one `str` object for repeated map keys.

## 2.0.9 - 2019-09-22

### Changed

- Minor performance improvements.

### Fixed

- Fix inaccurate zero padding in serialization of microseconds on
`datetime.time` objects.

## 2.0.8 - 2019-09-18

### Fixed

- Fix inaccurate zero padding in serialization of microseconds on
`datetime.datetime` objects.

## 2.0.7 - 2019-08-29

### Changed

- Publish PEP 517 source distribution.

### Fixed

- `orjson.dumps()` raises `JSONEncodeError` on circular references.

## 2.0.6 - 2019-05-11

### Changed

- Performance improvements.

## 2.0.5 - 2019-04-19

### Fixed

- Fix inaccuracy in deserializing some `float` values, e.g.,
31.245270191439438 was parsed to 31.24527019143944. Serialization was
unaffected.

## 2.0.4 - 2019-04-02

### Changed

- `orjson.dumps()` now serializes `datetime.datetime` objects without a
`tzinfo` rather than raising `JSONEncodeError`.

## 2.0.3 - 2019-03-23

### Changed

- `orjson.loads()` uses SSE2 to validate `bytes` input.

## 2.0.2 - 2019-03-12

### Changed

- Support Python 3.5.

## 2.0.1 - 2019-02-05

### Changed

- Publish Windows wheel.

## 2.0.0 - 2019-01-28

### Added

- `orjson.dumps()` accepts a `default` callable to serialize arbitrary
types.
- `orjson.dumps()` accepts `datetime.datetime`, `datetime.date`,
and `datetime.time`. Each is serialized to an RFC 3339 string.
- `orjson.dumps(..., option=orjson.OPT_NAIVE_UTC)` allows serializing
`datetime.datetime` objects that do not have a timezone set as UTC.
- `orjson.dumps(..., option=orjson.OPT_STRICT_INTEGER)` available to
raise an error on integer values outside the 53-bit range of all JSON
implementations.

### Changed

- `orjson.dumps()` no longer accepts `bytes`.

## 1.3.1 - 2019-01-03

### Fixed

- Handle invalid UTF-8 in str.

## 1.3.0 - 2019-01-02

### Changed

- Performance improvements of 15-25% on serialization, 10% on deserialization.

## 1.2.1 - 2018-12-31

### Fixed

- Fix memory leak in deserializing dict.

## 1.2.0 - 2018-12-16

### Changed

- Performance improvements.

## 1.1.0 - 2018-12-04

### Changed

- Performance improvements.

### Fixed

- Dict key can only be str.

## 1.0.1 - 2018-11-26

### Fixed

- pyo3 bugfix update.

## 1.0.0 - 2018-11-23

### Added

- `orjson.dumps()` function.
- `orjson.loads()` function.
