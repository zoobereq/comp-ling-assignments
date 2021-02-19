#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 13:55:00 2019

@author: zub
"""
class Employee:
    def __init__(self, name: str, title: str, employee_id: int):
        self.name = name
        self.title = title
        self.employee_id = employee_id

from typing import Iterator

def read_employees(path: str) -> Iterator[Employee]:
    with open(path, 'r') as source:
        while True:
            name = source.readline().replace('\n', '')
            if not name: #when you get to the end of the file python returns an empty string, and since that's the only time we're ever gonna get that, let's get rid of it
                break
            title = source.readline().replace('\n', '')
            employee_id = source.readline().replace('\n', '')
            source.readline() # if the next line is empty, it'll break
            yield Employee(name, title, int(employee_id))

def main():
    employees = read_employees('employees.txt')
    for employee in employees:
        print(f'Employee: Name: {employee.name}, Title: {employee.title}, ID: {employee.employee_id}')

main()
