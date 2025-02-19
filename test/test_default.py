# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# coding=UTF-8

import unittest
import uuid

import orjson


class Recursive:
    def __init__(self, cur):
        self.cur = cur


def default(obj):
    if obj.cur != 0:
        obj.cur -= 1
        return obj
    return obj.cur


class TypeTests(unittest.TestCase):
    def test_default_not_callable(self):
        """
        dumps() default not callable
        """
        with self.assertRaises(orjson.JSONEncodeError):
            orjson.dumps(uuid.uuid4(), default=NotImplementedError)

    def test_default_func(self):
        """
        dumps() default function
        """
        ref = uuid.uuid4()

        def default(obj):
            return str(obj)

        self.assertEqual(
            orjson.dumps(ref, default=default), b'"%s"' % str(ref).encode("utf-8")
        )

    def test_default_func_none(self):
        """
        dumps() default function None ok
        """
        self.assertEqual(orjson.dumps(uuid.uuid4(), default=lambda x: None), b"null")

    def test_default_func_exc(self):
        """
        dumps() default function raises exception
        """

        def default(obj):
            raise NotImplementedError

        with self.assertRaises(orjson.JSONEncodeError):
            orjson.dumps(uuid.uuid4(), default=default)

    def test_default_func_nested_str(self):
        """
        dumps() default function nested str
        """
        ref = uuid.uuid4()

        def default(obj):
            return str(obj)

        self.assertEqual(
            orjson.dumps({"a": ref}, default=default),
            b'{"a":"%s"}' % str(ref).encode("utf-8"),
        )

    def test_default_func_list(self):
        """
        dumps() default function nested list
        """
        ref = uuid.uuid4()

        def default(obj):
            if isinstance(obj, uuid.UUID):
                return [str(obj)]

        self.assertEqual(
            orjson.dumps({"a": ref}, default=default),
            b'{"a":["%s"]}' % str(ref).encode("utf-8"),
        )

    def test_default_func_nested_list(self):
        """
        dumps() default function list
        """
        ref = uuid.uuid4()

        def default(obj):
            return str(obj)

        self.assertEqual(
            orjson.dumps([ref] * 100, default=default),
            b"[%s]"
            % b",".join((b'"%s"' % str(ref).encode("utf-8") for _ in range(100))),
        )

    def test_default_func_bytes(self):
        """
        dumps() default function errors on non-str
        """
        ref = uuid.uuid4()

        def default(obj):
            return bytes(obj)

        with self.assertRaises(orjson.JSONEncodeError):
            orjson.dumps(ref, default=default)

    def test_default_func_invalid_str(self):
        """
        dumps() default function errors on invalid str
        """
        ref = uuid.uuid4()

        def default(obj):
            return "\ud800"

        with self.assertRaises(orjson.JSONEncodeError):
            orjson.dumps(ref, default=default)

    def test_default_lambda_ok(self):
        """
        dumps() default lambda
        """
        ref = uuid.uuid4()
        self.assertEqual(
            orjson.dumps(ref, default=lambda x: str(x)),
            b'"%s"' % str(ref).encode("utf-8"),
        )

    def test_default_callable_ok(self):
        """
        dumps() default callable
        """

        class CustomSerializer:
            def __init__(self):
                self._cache = {}

            def __call__(self, obj):
                if obj not in self._cache:
                    self._cache[obj] = str(obj)
                return self._cache[obj]

        ref_obj = uuid.uuid4()
        ref_bytes = b'"%s"' % str(ref_obj).encode("utf-8")
        for obj in [ref_obj] * 100:
            self.assertEqual(orjson.dumps(obj, default=CustomSerializer()), ref_bytes)

    def test_default_recursion(self):
        """
        dumps() default recursion limit
        """
        self.assertEqual(orjson.dumps(Recursive(5), default=default), b"0")

    def test_default_recursion_reset(self):
        """
        dumps() default recursion limit reset
        """
        self.assertEqual(
            orjson.dumps(
                [Recursive(5), {"a": "b"}, Recursive(5), Recursive(5)], default=default
            ),
            b'[0,{"a":"b"},0,0]',
        )

    def test_default_recursion_infinite(self):
        """
        dumps() default infinite recursion
        """
        ref = uuid.uuid4()

        def default(obj):
            return obj

        with self.assertRaises(orjson.JSONEncodeError):
            orjson.dumps(ref, default=default)
