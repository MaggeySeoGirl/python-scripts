#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Cover Letter Generator

This plugin generates customized cover letters for different professions and job roles using the OpenAI API.

"""

import openai

def generate_cover_letter(profession, job_role):
  # Use the OpenAI API to generate a cover letter based on the inputs
  cover_letter = openai.generate_text(profession, job_role)
  return cover_letter

