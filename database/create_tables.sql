CREATE TABLE authors (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE papers (
  id INT NOT NULL AUTO_INCREMENT,
  author INT NOT NULL,
  title TEXT NOT NULL,
  abstract TEXT NOT NULL,
  publication VARCHAR(255) NOT NULL,
  pub_date DATE NOT NULL,
  source VARCHAR(255) NOT NULL,
  doi VARCHAR(255),
  arxiv_id VARCHAR(255),
  scopus_id VARCHAR(255),
  ads_id VARCHAR(255),
  PRIMARY KEY (id),
  FOREIGN KEY (author) REFERENCES authors(id),
  UNIQUE (doi),
  UNIQUE (arxiv_id),
  UNIQUE (scopus_id),
  UNIQUE (ads_id)
);

CREATE TABLE refs (
  subject_paper_id INT NOT NULL,
  object_paper_id INT NOT NULL,
  FOREIGN KEY (subject_paper_id) REFERENCES papers(id),
  FOREIGN KEY (object_paper_id) REFERENCES papers(id),
  PRIMARY KEY (subject_paper_id, object_paper_id)
);

CREATE TABLE paper_authors (
  paper_id INT NOT NULL,
  author_id INT NOT NULL,
  FOREIGN KEY (paper_id) REFERENCES papers(id),
  FOREIGN KEY (author_id) REFERENCES authors(id),
  PRIMARY KEY (paper_id, author_id)
);

CREATE TABLE paper_keywords(
  paper_id INT NOT NULL,
  keyword VARCHAR(255) NOT NULL,
  FOREIGN KEY (paper_id) REFERENCES papers(id),
  PRIMARY KEY (paper_id, keyword)
);
